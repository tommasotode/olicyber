undefined8 main(EVP_PKEY_CTX *param_1)
{
  char choice;
  long in_FS_OFFSET;
  char unsafebuf [40];
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  inutile(param_1);
  while( true ) {
    while( true ) {
      while( true ) {
        while( true ) {
          print_menu();
          choice = read_choice();
          if (choice != '1') break;
          printf("Give me the stack data: ");
          gets(unsafebuf);
        }
        if (choice != '2') break;
        printf("Give me the global data: ");
        gets(global_buf);
      }
      if (choice != '3') break;
      print_canary();
    }
    if (choice == '4') break;
    puts("Unknown option");
  }
  puts("Bye!");
  if (canary != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}