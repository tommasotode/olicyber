import angr
import claripy

max_flag_len = 30
succ_addr = 0x1ef8
fail_addr = 0x1f02

def solve(max_len, succaddr, failaddr):
    p = angr.Project("./ObscureSecurity", auto_load_libs=False)
    
    chars = [claripy.BVS(f'c{i}', 8) for i in range(max_len)]
    flag = claripy.Concat(*chars + [claripy.BVV(0, 8)])
    
    state = p.factory.full_init_state(args=["./source", flag])
    
    for c in chars:
        state.solver.add(claripy.Or(c == 0, claripy.And(c >= 0x20, c <= 0x7e)))
    
    state.solver.add(claripy.Or(*[c == 0 for c in chars]))
    
    sim = p.factory.simulation_manager(state)
    sim.explore(find=succaddr, avoid=failaddr)
    
    if sim.found:
        sol = sim.found[0].solver.eval(flag, cast_to=bytes)
        flag_end = sol.find(b'\0')
        print("sol found:", sol[:flag_end])
    else:
        print("no sol")

solve(max_flag_len, succ_addr, fail_addr)