import angr
import claripy

proj = angr.Project('binary/controllo_ricorsivo_circa', auto_load_libs=False)

flag_chars = [claripy.BVS(f'flag_{i}', 8) for i in range(29)]
flag = claripy.Concat(*flag_chars)

state = proj.factory.full_init_state(stdin=flag)

for k in flag_chars:
    state.solver.add(k >= 0x20)
    state.solver.add(k <= 0x7e)

simgr = proj.factory.simulation_manager(state)

def is_successful(state):
    output = state.posix.dumps(1)
    return b'flag' in output

def is_failure(state):
    output = state.posix.dumps(1)
    return b'Nope!' in output

simgr.explore(find=is_successful, avoid=is_failure)

if simgr.found:
    found = simgr.found[0]
    solution = found.solver.eval(flag, cast_to=bytes)
    print(f'[+] Flag: {solution.decode()}')
else:
    print('[-] No solution found.')
