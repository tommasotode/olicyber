undefined1 read_choice(void)
{
  int bufsize;
  long in_FS_OFFSET;
  undefined1 inbuf;
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  printf("Enter option: ");
  do {
    bufsize = scanf("%c%*c",&inbuf);
  } while (bufsize != 1);
  if (canary != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return inbuf;
}