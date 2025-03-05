void print_canary(void)
{
  long in_FS_OFFSET;
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  if (global_magic == 0x1337) {
    printf("Take this gift: 0x%lx\n",canary);
  }
  else {
    puts("Nope");
  }
  if (canary != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}