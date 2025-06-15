void print_menu(void)
{
  long in_FS_OFFSET;
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  puts("[MENU]:");
  puts("> [1] BOF Stack");
  puts("> [2] BOF Data");
  puts("> [3] Gift");
  puts("> [4] Exit");
  puts("=================================");
  if (canary != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}