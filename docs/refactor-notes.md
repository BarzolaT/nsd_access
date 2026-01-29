# Package update

+ I update the packaging, by changing to `pyproject.toml`.
+ The package is not fully pip installable (because of `pycocotools`). I add a makefile to help the installation
+ I remove unused library, `nsdcode` latest version does not require `scikit-learn` but it was not applied to the pip version. I change to the github version>

# Organization Refactor

To improve life expectancy of the project I propose to devide the class into submodules with different behaviors.
To keep a class like behavior, each module is attributed to an attribute in the class.

e.g.

```{python}
handler = nsda.nsda("Path/to/nsd")
behavior_dataframe = handler.behavior.read_behavior("subj01")
```
# Utils

## safe_coco_import

Since pycocotools is not pip installable, I add this utilitary to check the import when needed.

## subject_identifier

To simplify subject call, allows easily various form of calling subjects.
```
>>> subject_identifier(1)
'subj01'
>>> subject_identifier('subj1')
ValueError: Subject subj1 is not a valid nsd subject
>>> subject_identifier(10)
ValueError: Subject number 10 does not exist
```


# Behavior

## read_behavior

+ Added the filter by session to be the same as the filter by trial.
+ Default values will return the whole dataframe

## get_repeated_conditions

Added because it is used most nsd-related project. 


# Downloader

Used to download nsd and coco file.

# NSDA

## read_image_coco_info

+ I remove the difference of behavior for one and >1 images.
+ I remove the shows options ot be consistent with the >1 image case.
+ I keep the behavior that it will always return a list of dict. In my opinion it is a bad behavior, and it should return a dict of list, but I think it makes more sense with the pycocotools package.



