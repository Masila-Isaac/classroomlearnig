
void main() {
  int x = 41;
  print(x);
  String firstname = "isaac";
  print("string: $firstname");
  double decimal = 195.5;
  print(decimal);
  bool miller = true;
  print(miller);
  dynamic fullname = "isaac masila ";
  print(fullname);
  var emptylist = [];
  print(emptylist);
  emptylist.addAll([1, 2, 3, 4]);
  print(emptylist);
  emptylist[0] = "masila";
  print(emptylist);
  emptylist.insert(4, "miller");
  print(emptylist);
  emptylist.insertAll(1, ["mercy", "mercy", 8, 9, 11, "siscah"]);
  print(emptylist);
  emptylist.remove("mercy");
}
