void write_qword(void)
{
  long in_FS_OFFSET;
  ulong *address;
  ulong content;
  ulong paddedcontent;
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  puts("where: ");
  __isoc99_scanf(&lx,&address);
  puts("what: ");
  __isoc99_scanf(&lx,&content);
  paddedcontent = content ^ write_key;
  *address = paddedcontent;
  if (canary != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

