scancel -u rli12314
for i in {1..7}
do
  rm *${i}.sh
done
rm *.out
rm -rf storage/*
