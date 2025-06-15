key1 = "JIiEv3";
int check_1(long p)
{
  char c [6];
  
  for (int i = 0; i < 6; i++) {
    c[i] = p[i] + '\x04';
  }
  int ret = strncmp(key_1, c, 6);

  return ret != 0;
}

key2 = "Kg9FRj";
int check_2(long p)
{
  char c [6];
  
  for (int i = 0; i < 6; i++) {
    c[i] = p[i] ^ 6;
  }
  int ret = strncmp(key_2, c, 6);

  return ret != 0;
}

key3 = "xe8zh2";
int check_3(long p1)
{
  char c [6];
  
  for (int i = 0; i < 6; i++) {
    c[i] = p1[map[i]];
  }
  int ret = strncmp(key_3, c, 6);

  return ret != 0;
}
