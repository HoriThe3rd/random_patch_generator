Unlabeled Patch Generator
=======

## Overview
パッチ画像をランダムに自動生成するためのスクリプトである．[Image_Patch_Generator](https://github.com/RxstydnR/Image_Patch_Generator)を参考に作成した．

## Execution
実行は次のように行う．
```txt
python unlabeled_patch_generator.py \
--dataset ./images_test \
--save_dir ./unlabeled \
--patch_width 45 --patch_height 45 \
--num 10
```

`--num`オプションは各画像から切り出すパッチの枚数を示す．

これを実行すると，`--save_dir`で指定したフォルダが自動生成され，その中に，`marked`と`patches`の二つのフォルダが生成される．
なお，`--save_dir`オプションに既存のフォルダを指定するとエラーとなる．

`marked`には画像のどこからパッチを切り出したかを示す赤い四角形が書き込まれた画像ファイルが保存されている．

`patches`には実際に切り出されたパッチ画像が保存される．

## Branches
開発は専ら`dev`ブランチにおいて行う．動作するバージョンができたら`main`ブランチにマージする．
| Branch name | Role       |
| ----------- | ---------- |
| main        | リリース版   |
| dev         | 開発中      |