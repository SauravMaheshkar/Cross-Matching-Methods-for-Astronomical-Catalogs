import streamlit as st
from utils import import_bss, import_super, crossmatch
from PIL import Image

ukst_image = Image.open('UKST.jpg')
atca_image = Image.open('ATCA.jpg')
coordinate_system = Image.open('coordinate.jpg')
@st.cache(suppress_st_warning=True)
def load_data():
    bss_cat = import_bss()
    super_cat = import_super()
    return bss_cat, super_cat

st.title("Cross Matching Methods for Astronomical Catalogs")

st.sidebar.title("Aim")
st.sidebar.subheader("To explore methods of positional cross-matching for object detection by comparing data from multiple telescopes at different wavelengths")
st.sidebar.title("Data Sources")
st.sidebar.markdown("Radio Survey : [AT20G Bright Source Sample (BSS) catalogue](http://cdsarc.u-strasbg.fr/viz-bin/Cat?J/MNRAS/384/775)")
st.sidebar.markdown("Optical Survey : [SuperCOSMOS all-sky galaxy catalogue](http://ssa.roe.ac.uk/allSky)")
st.sidebar.markdown("By [Saurav Maheshkar](https://github.com/SauravMaheshkar)")

st.markdown("---")

st.header("Introduction 👋")
st.markdown("In observational astronomy, after the raw data are produced from telescopes, they are processed to extract celestial objects, or called **sources**. The information, e.g., positions and light intensity of these sources, are stored in a tabular format to facilitate further analysis. One central operation on these astronomical catalogs is cross-match, **generating matches of the same object from multiple catalogs**. Through this operation, astronomers can integrate catalogs from various instruments observed at different points of time to examine a unioned set of properties or to study the [temporal evolution](http://adsabs.harvard.edu/full/1909PA.....17..418M) for each object. \n \n With the development of high-resolution detectors and large array of cameras, the state-of-the-art sky survey projects produce and archive astronomical catalogs of vast number of objects. Cross-matching these billion-scale catalogs are both data- and computation-expensive, yet a fast matching time is desirable to astronomical studies and is mandatory to real-time astronomical missions.")

st.image(ukst_image, caption='UK Schmidt Telescope',
use_column_width=True)

st.markdown(""" This operation corresponds to what in database terminology is called a **join**.\n \n

But, there are various complexities to specifying such a match.

1. First, we have to define what is the condition that must be satisfied for two rows to be considered matching.
2. Then, we must decide what happens if, for a given row, more than one match can be found.
3. Finally, we have to decide what to do having worked out what the matched rows are; the result will generally be presented as a new output table, but there are various choices about what columns and rows it will consist of.

""")

st.markdown("---")

st.header("ℹ️ Methodology")

st.image(coordinate_system, caption='The celestial coordinate system',
use_column_width=True)

st.markdown("The positions of stars, galaxies and other astronomical objects are usually recorded in either equatorial or Galactic coordinates. \n \n Equatorial coordinates are fixed relative to the celestial sphere, so the positions are independent of when or where the observations took place They are defined relative to the celestial equator (which is in the same plane as the Earth's equator) and the ecliptic (the path the sun traces throughout the year). \n \n A point on the celestial sphere is given by two coordinates:\n \n  * **Right ascension**: the angle from the vernal equinox to the point, going east along the celestial equator \n \n * **Declination**: the angle from the celestial equator to the point, going north (negative values indicate going south). \n \n \n \n  The vernal equinox is the intersection of the celestial equator and the ecliptic where the ecliptic rises above the celestial equator going further east. ")

st.markdown("---")

st.header("Conversions Used")
st.subheader("hms2dec")
st.markdown("Right ascension is often given in **hours-minutes-seconds** (HMS) notation, because it was convenient to calculate when a star would appear over the horizon. A full circle in HMS notation is 24 hours, which means 1 hour in HMS notation is equal to 15 degrees. \n \n Each hour is split into 60 minutes and each minute into 60 seconds. \n \n We can convert 23 hours, 12 minutes and 6 seconds (written as `23:12:06` or `23h12m06s`) to degrees like :")
st.latex(r"15 \times(23 + \frac{12}{60} + \frac{6}{60 \times 60} )")
st.subheader("dms2dec")
st.markdown("Declination, on the other hand, is traditionally recorded in **degrees-minutes-seconds** (DMS) notation. A full circle is 360 degrees, each degree has 60 arcminutes and each arcminute has 60 arcseconds. \n \n For example: 73 degrees, 21 arcminutes and 14.4 arcseconds (written `73:21:14.4` or `73d21m14.4s`) can be converted to decimal degrees like:")
st.latex(r"73 + \frac{21}{60} + \frac{14.4}{60 \times 60}")

st.markdown("---")

st.header("Calculating Distance")

st.write(r"""
To crossmatch two catalogues we need to compare the angular distance between objects on the celestial sphere. If we have an object on the celestial sphere with right ascension and declination ($\alpha1$,$\delta1$), then the angular distance to another object with coordinates ($\alpha2$,$\delta2$) is given by the **haversine** formula:

$$
d = 2 \arcsin (\sqrt{sin^2 \frac{|\delta_1 - \delta_2|}{2} + cos \delta_1 cos\delta_2sin^2\frac{|\alpha_1 - \alpha_2|}{2}})
$$

We make a function that selects an object from the radio survey (BSS) and iterates through all the objects in the SuperCOSMOS survey and finds the closest match as per user-defined threshold.
""")

st.markdown("---")

st.header("Data")
st.markdown("""Data used in this project comes from two surveys:

- Radio Survey : [AT20G Bright Source Sample (BSS) catalogue](http://cdsarc.u-strasbg.fr/viz-bin/Cat?J/MNRAS/384/775)
- Optical Survey : [SuperCOSMOS all-sky galaxy catalogue](http://ssa.roe.ac.uk/allSky)""")

st.image(atca_image, caption='Five of the ATCA antennas at Narrabri',
use_column_width=True)

st.markdown("""The BSS catalogue lists the brightest sources from the AT20G radio survey while the SuperCOSMOS catalogue lists galaxies observed by visible light surveys. If we can find an optical match for our radio source, we are one step closer to working out what kind of object it is, e.g. a galaxy in the local Universe or a distant quasar. \n \n

The data sources vary considerably in their sizes. BSS has only 320 objects whereas the SuperCOSMOS has around 240 million objects. \n \n

Thus, we can illustrate the issues one can encounter when implementing cross-matching algorithms.
""")

st.markdown("---")

st.header("Demo ‍‍👨‍💻")
st.markdown("Try the project out for yourself by clicking the button below. **BEWARE** this will start importing the dataset and can take upto 1 to 2 minutes to load so be patient")

if st.button("Try out the Project"):
    bss_cat, super_cat = load_data()
    max_dist = st.number_input("Maximum Distance in arcseconds")
    matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
    st.text("Best Match")
    st.write("Radio Object ID: ",matches[0][0] )
    st.write("Optical Object ID: ",matches[0][1])
    st.write("Distance between them: ",matches[0][2])

st.markdown("---")

st.markdown("If you want to contribute to the project or are interested in the code kindly check out the **Github repository [here](https://github.com/SauravMaheshkar/Cross-Matching-Methods-for-Astronomical-Catalogs) **, show some love ❤️ by starring the repository and support me. 😊")
