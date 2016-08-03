# birth_records
To get count of obstetric estimate number of weeks at gestation:
cat Nat2014PublicUS.c20150514.r20151022.txt| cut -c 499-500 | sort -n | uniq -c
