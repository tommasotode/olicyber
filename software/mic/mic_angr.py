#!/usr/bin/env python3
import angr
import claripy

def main():
    p = angr.Project('MIC')

    key_chars = [claripy.BVS('key_%d' % i, 8) for i in range(36)]
    key = claripy.Concat(*key_chars + [claripy.BVV(b'\n')])

    st = p.factory.full_init_state(
            args=['./MIC'],
            add_options=angr.options.unicorn,
            stdin=key
    )

    # key characters must be printable
    for k in key_chars:
        st.solver.add(k >= 0x21)
        st.solver.add(k <= 0x7e)
        # st.solver.add(k != ord('L')) # if the letter L was banned

    sm = p.factory.simulation_manager(st)
    sm.run()

    for pp in sm.deadended:
        out = pp.posix.dumps(1)
        if b'Message decrypted correctly.' in out:
            return pp.solver.eval(key, cast_to=bytes).decode().strip()

    return ''

def test():
    main()

if __name__ == "__main__":
    print(main())
