#!/usr/bin/env python3
import angr
import claripy

def main():
    p = angr.Project('justonekey')

    key_chars = [claripy.BVS('key_%d' % i, 8) for i in range(31)]
    key = claripy.Concat(*key_chars + [claripy.BVV(b'\n')])

    st = p.factory.full_init_state(stdin=key)

    for k in key_chars:
        st.solver.add(k >= 0x21)
        st.solver.add(k <= 0x7e)

    sm = p.factory.simulation_manager(st)
    sm.run()

    for pp in sm.deadended:
        out = pp.posix.dumps(1)
        if b'Correct key' in out:
            return pp.solver.eval(key, cast_to=bytes).decode().strip()

    return ''

if __name__ == "__main__":
    print(main())