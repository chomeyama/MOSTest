# MOSTest


## Simple explanation of this opensource code (mainly for my lab members).

1. Create wav directory like below. Each set contains wav files and their file lists for the methods you want to compare.

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
 |      |-- method3/
 |      |-- method1.list
 |      |-- method2.list
 |      |-- method3.list
 |---- set3
 ```
 
2. Rewrite mos.js depending on the structure of the wav directory. You may have to change lines 44-54 (filepathes are hard coded) and lines 194- (settings).

3. Rewrite index.html as you like. Note that my email address is written, so you may have to change it to your own contact information.

4. Finally, use github pages and choose index.html for the source to deploy your own test. The test automatically emits a csv file when the test finishes.

If you want to conduct another test (not MOS test), you may have to change mos.js and index.html depending on the test.
Please feel free to ask any questions you may have by slack or in person.
