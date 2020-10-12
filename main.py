import streamlit as st
from utils import import_bss, import_super, crossmatch

st.title("Cross Matching Methods for Astronomical Catalogs")

@st.cache(suppress_st_warning=True)
def load_data():
    bss_cat = import_bss()
    super_cat = import_super()
    return bss_cat, super_cat
bss_cat, super_cat = load_data()

st.sidebar.title("Aim")
st.sidebar.subheader("To explore methods of positional cross-matching for object detection by comparing data from multiple telescopes at different wavelengths")
st.sidebar.title("Data Sources")
st.sidebar.markdown("Radio Survey : [AT20G Bright Source Sample (BSS) catalogue](http://cdsarc.u-strasbg.fr/viz-bin/Cat?J/MNRAS/384/775)")
st.sidebar.markdown("Optical Survey : [SuperCOSMOS all-sky galaxy catalogue](http://ssa.roe.ac.uk/allSky)")
st.sidebar.markdown("By [Saurav Maheshkar](https://github.com/SauravMaheshkar)")

st.header("Try for yourself")

max_dist = st.number_input("Maximum Distance in arcseconds")
if st.button("Crossmatch Catalogs"):
    matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
    st.text("Best Match")
    st.write("Radio Object ID: ",matches[0][0] )
    st.write("Optical Object ID: ",matches[0][1])
    st.write("Distance between them: ",matches[0][2])
    
st.header("Methodology")
st.markdown("The positions of stars, galaxies and other astronomical objects are usually recorded in either equatorial or Galactic coordinates. \n \n Equatorial coordinates are fixed relative to the celestial sphere, so the positions are independent of when or where the observations took place They are defined relative to the celestial equator (which is in the same plane as the Earth's equator) and the ecliptic (the path the sun traces throughout the year). \n \n A point on the celestial sphere is given by two coordinates:\n \n  * **Right ascension**: the angle from the vernal equinox to the point, going east along the celestial equator \n \n * **Declination**: the angle from the celestial equator to the point, going north (negative values indicate going south). \n \n \n \n  The vernal equinox is the intersection of the celestial equator and the ecliptic where the ecliptic rises above the celestial equator going further east. ")
st.header("Conversions Used")
st.subheader("hms2dec")
st.markdown("Right ascension is often given in hours-minutes-seconds (HMS) notation, because it was convenient to calculate when a star would appear over the horizon. A full circle in HMS notation is 24 hours, which means 1 hour in HMS notation is equal to 15 degrees. \n \n Each hour is split into 60 minutes and each minute into 60 seconds.")
st.subheader("dms2dec")
st.markdown("Declination, on the other hand, is traditionally recorded in **degrees-minutes-seconds** (DMS) notation. A full circle is 360 degrees, each degree has 60 arcminutes and each arcminute has 60 arcseconds.")
st.latex("73+\frac{21}{60}+\frac{14.4}{60\times60}")
st.header("Calculating Distance")
st.markdown("To crossmatch two catalogues we need to compare the angular distance between objects on the celestial sphere. \n \n People loosely call this a 'distance', but technically its an angular distance")
