from pwn import *
import re

HOST = "codevincictf.itis.pr.it"
PORT = 9969
FAKE_FLAG = "CodeVinciCTF{I'm_not_the_real_flag_uwu}"

context.log_level = 'info'

def query_path(path):
    conn = remote(HOST, PORT)
    conn.sendlineafter(b"connections", path.encode())
    response = conn.recvall().decode()
    conn.close()
    
    return response

def get_branches_and_leaf(path):
    response = query_path(path)
    
    branches = []
    leaf = None
    
    if "There are no connected branches or this branch" in response:
        leaf_match = re.search(r"Here is the leaf for this branch:\s*(.+)", response)
        if leaf_match:
            leaf = leaf_match.group(1).strip()
        return branches, leaf
    
    branch_list_match = re.search(r"Here is the list of the linked branches:\s*([\s\S]+?)(?:Here is the leaf for this branch:|$)", response)
    if branch_list_match:
        branch_list = branch_list_match.group(1).strip()
        branches = [branch.strip() for branch in branch_list.split('\n') if branch.strip()]
    
    leaf_match = re.search(r"Here is the leaf for this branch:\s*(.+)", response)
    if leaf_match:
        leaf = leaf_match.group(1).strip()
    
    return branches, leaf

def dfs_tree(path=""):
    if not path:
        path = "/"
    
    log.info(f"Exploring: {path}")
    
    branches, leaf = get_branches_and_leaf(path)
    
    if leaf and leaf != FAKE_FLAG:
        log.success(f"Found real flag: {leaf} at path: {path}")
        return leaf
    
    for branch in branches:
        new_path = path
        if path == "/":
            new_path = f"/{branch}"
        else:
            new_path = f"{path}/{branch}"
        
        flag = dfs_tree(new_path)
        if flag and flag != FAKE_FLAG:
            return flag
    
    return None

def main():
    try:
        real_flag = dfs_tree()
        if real_flag:
            log.success(f"done, flag: {real_flag}")
        else:
            log.error("No unique flag found. All leaves contained the fake flag.")
    except Exception as e:
        log.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()