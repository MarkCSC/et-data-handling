# IMAGES TO SNIPPETS TOOL
\*\***PLEASE READ THE WHOLE DOC BEFORE START**\*\*
## 1. INTRODUCTION
This tool crops images into many snippets and store in a directory.

It comes with a tracking file called ```process.txt``` which help program tracks whether the photo (path) has processed before in previous runs.

In case any crashes occured or you just want to take a rest during the cropping process, you don't have to start it all over again. with this tracking file.

## 2. __FILE STRUCTURE__
You __MUST__ have the following file structure to start using this tool

```
<your_dir>/
├── main.py
└── log/
```
The following file structure is __highly suggested__ (or you will have to input the args everytime by yourself)
```
<your_dir>/
├── main.py  # entry point
├── log/     # run logs
├── image/   # default dest for reading images
└── snip/    # default dest for stoging sinppets
```
---

## 3. __START USING__

### 3.1 Arguments

If you are using the recommened structure. 

The default directory for images to be cropped is ```<your_dir>/image/``` and the default snippets storage directory is ```<your_dir>/snip/``` 

Use this command for default settings:
```
python main.py
```
If you want to customize any of these directories

Replace the ```<image_dir_for_images>``` with your own folder for images

Replace ```<dir_to_store_snips>``` to the directory that you wish the snippets to stored in

> Both folders must exist in advanced

```
python main.py --image_dir <image_dir_for_images> --snip_dir <dir_to_store_snips>
```
>You can change only one of the arguments too e.g.
```
python main.py --image_dir <image_dir_for_images>
```

After the image show on the screen, no matter cropping or not, it will be treated as processed. The file path will be saved to the process.txt.

The image path stored in process.txt will **NOT** be processed in the future run as the programme assume you have already processed it before.

If you do not wish to store the photo path to process.txt, use the ```-i``` or ```--ignore``` flag

```
python main.py -i
```
or
```
python main.py --ignore
```

### 3.2 Cropping images

When the image shows on the secreen, you can hold and drag a rectangle out.

Press <kbd>s</kbd> to save the last rectangular region drawn.
If you do not want it, simply re-draw one or click any key other than the key specified below.

Press <kbd>Enter</kbd> to crop and exprot all the rectangular region. The next photo will appear (if applicable).

> Don't forget to save the last rectangle while cropping!!

| Key + Action| Function|
|:----:|:----:|
|<kbd>Left-Button</kbd> + <kbd>drag</kbd>|Draw a rectangular region|
|<kbd>s</kbd>|Saves the last rectangular region drawn|
|<kbd>Enter</kbd>|Export all selected region into snippets|

