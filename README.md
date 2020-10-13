![Banner](https://github.com/SauravMaheshkar/Cross-Matching-Methods-for-Astronomical-Catalogs/blob/master/Banner.png)

# Cross Matching Methods for Astronomical Catalogs

# Table of contents

- [Table of contents](#table-of-contents)
- [Aim](#aim)
- [Installation](#installation)
- [Usage](#usage)
- [Directory tree](#directory-tree)
- [Request](#request)
    -[Bug](#bug)
- [Contribute](#contribute)
- [License](#license)
- [Credits](#credits)

# Aim
[(Back to top)](#table-of-contents)

To explore methods of positional cross-matching for object detection by comparing data from multiple telescopes at different wavelengths

# Installation
[(Back to top)](#table-of-contents)

To use this project, first clone the repo on your device using the command below:

```git init```

```https://github.com/SauravMaheshkar/Cross-Matching-Methods-for-Astronomical-Catalogs.git``` 

You'll also need to run the ```requirements.txt``` file to download all the dependencies. Then you can run the app by running ```streamlit run main.py```. This will open a web app where you'll need to put in the threshold value for the minimum angular distance.

# Usage
[(Back to top)](#table-of-contents)

To run the program just run the following command on the terminal
```python
streamlit run main.py
```

# Directory Tree
[(Back to top)](#table-of-contents)

```bash
├── README.md
├── __pycache__
│   └── utils.cpython-38.pyc
├── data
│   ├── BSS.dat
│   └── SuperCOSMOS.csv
├── docker-compose.yml
├── main.py
├── requirements.txt
├── setup.sh
└── utils.py
```

# Request
[(Back to top)](#table-of-contents)

### Bug 
[(Back to top)](#table-of-contents)

If you spot a bug in the program kindly raise a issue. Instructions for raising an issue can be found [here](https://docs.github.com/en/enterprise/2.15/user/articles/creating-an-issue)

# Contribute
[(Back to top)](#table-of-contents)

If you want to contribute to the project kindly mail me at `sauravvmaheshkar@gmail.com`.

### Step 1
 - **Option 1**
   🍴 Fork it!  
 - **Option 2**
    👯‍♂️ Clone this repo to your local machine using `https://github.com/SauravMaheshkar/Cross-Matching-Methods-for-Astronomical-Catalogs.git`
### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request using `https://github.com/SauravMaheshkar/Cross-Matching-Methods-for-Astronomical-Catalogs/compare/`


# License
[(Back to top)](#table-of-contents)

[![License](http://img.shields.io/:license-mit-blue.svg)](http://doge.mit-license.org)

The data for this project was taken from:

* **Radio Survey** : [AT20G Bright Source Sample (BSS) catalogue](http://cdsarc.u-strasbg.fr/viz-bin/Cat?J/MNRAS/384/775)

* **Optical Survey** : [SuperCOSMOS all-sky galaxy catalogue](http://ssa.roe.ac.uk/allSky)

- Copyright 2020 @[Saurav Maheshkar](https://sauravvmaheshkar.gitbook.io/saurav-maheshkar/)
- [MIT License](https://opensource.org/licenses/MIT)


# Credits

The inspiration for this readme file came from
- [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46#license)
- [Navendu Pottekkat](https://github.com/navendu-pottekkat/awesome-readme/blob/master/README-template.md)

Description of the CoxPH came froom
- [Wikipedia](https://en.wikipedia.org/wiki/Proportional_hazards_model)
- [Statsdirect](https://www.statsdirect.com/help/survival_analysis/cox_regression.htm)
