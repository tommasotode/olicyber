undefined8 main(EVP_PKEY_CTX *param_1)
{
  long in_FS_OFFSET;
  int input;
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  input = 0;
  puts("Welcome to our r/w playground!");
  printf("A little gift for you... %p\n",&input);
  while( true ) {
    while( true ) {
      while( true ) {
        print_menu();
        __isoc99_scanf(&u,&input);
        if (input != 1) break;
        read_qword();
      }
      if (input != 2) break;
      write_qword();
    }
    if (input != 3) break;
    puts("Mmmm no, jk.");
  }
  puts("Invalid choice!");
  if (canary != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 1;
}