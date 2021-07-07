# MOSTest

## Simple explanation of this opensource code (mainly for my lab members).

1. Create wav directory like below. Each set contains wav files and their file lists for the methods you want to compare. The number of methods in each set does not have to match.

```
wav/
 |---- set1/
 |      |-- method1/
 |      |-- method2/
 |      |-- method3/
 |      |-- method1.list
 |      |-- method2.list
 |      |-- method3.list
 |
 |---- set2
 |      |-- method1/
 |      |-- method2/
 |      |-- method1.list
 |      |-- method2.list
 |
 |---- set3
 ```

2. Rewrite mos.js depending on the structure of the wav directory. You only need to customize the part from line 60.

3. Rewrite index.html as you like. Note that my email address is written as contact info, so you may have to change it to your own one.

4. Use Github Pages to deploy your own test. The test automatically emits a csv file when the test finishes.

If you want to conduct tests other than a MOS test, you need to modify the code significantly depending on the test.

Please feel free to ask any questions you may have by slack or in person.
