void read_qword(void)
{
  long in_FS_OFFSET;
  ulong *address;
  ulong paddedaddress;
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  puts("where: ");
  __isoc99_scanf(&lx,&address);
  paddedaddress = read_key ^ *address;
  printf("value: 0x%lx\n",paddedaddress);
  if (canary != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}