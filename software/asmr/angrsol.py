import angr
import claripy

def solve(flaglen, succaddr, failaddr):
    p = angr.Project("software/asmr/asmr", auto_load_libs=False)
    
    chars = [claripy.BVS(f'c{i}', 8) for i in range(flaglen)]
    flag = claripy.Concat(*chars + [claripy.BVV(b'\n')])

    state = p.factory.full_init_state(stdin=flag)
    for c in chars:
        state.solver.add(c >= 0x20) # ' '
        state.solver.add(c <= 0x7e) # '~'

    sim = p.factory.simulation_manager(state)
    sim.explore(find=succaddr, avoid=failaddr)

    if len(sim.found) > 0:
        sol = sim.found[0].solver.eval(flag, cast_to=bytes)
        print("sol found:", sol[:flaglen])
    else:
        print("no sol")

solve(25, 0x08049429, 0x08049478)