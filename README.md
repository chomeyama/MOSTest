# MOSTest

## Simple explanation of this opensource

1. Create wav directory like the below example. Each set contains wav files and their file lists for the methods you want to compare. It's easier to understand if you actually browse the wav directory. The number of methods in each set does not have to be identical.

```
wav/
 |---- set1/
 |      |-- method1/
 |      |     |-- sample1.wav
 |      |     |-- sample2.wav
 |      |-- method2/
 |      |     |-- sample1.wav
 |      |     |-- sample2.wav
 |      |-- method1.list
 |      |-- method2.list
 |
 |---- set2
 |      |
 ```

 The command ```find wav/set1 -name "*.wav" | grep "method1" > wav/set1/method1.list``` would be helpful to create list files.

2. Rewrite mos.js depending on the structure of the wav directory. You only need to customize the part from line 45.

3. Rewrite index.html as you like.

4. Use some server you can deploy this code. If you are not familiar with this kind of thing, Github Pages would be easy to use.

5. If subjects finish the test, a csv file is automatically emitted.

You can utilize [ABXTest](https://github.com/chomeyama/ABXTest) if you want to conduct ABX test.
