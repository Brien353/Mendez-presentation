import streamlit as st
import pandas as pd


st.title("Mendez-Guadalupe-Zacatecas")

with st.expander("Localization",type= "default"):
    st.subheader("Geography")
    lat = 22 + (55 / 60) + (53.755 / 3600)  
    lon = -(102 + (16 / 60) + (23.430 / 3600)) 
    df = pd.DataFrame({"lat": [lat], "lon": [lon]})
    st.map(df)
    st.write("Longitude: 102°16'23.430\" W | Latitude: 22°55'53.755\" N")


with st.expander("Demographics & Housing Overview"):
  st.subheader("Population Details")
  st.image("https://images.ctfassets.net/pdf29us7flmy/1GhdfeSI5sC5aBEmEPaFaD/4480ef2730a6d2f7a1aaa1ac727b8fcd/Hero_Illustration_-_Swap_Component.png?w=720&q=100&fm=jpg", width=300)
  st.text("Total Population: 33 inhabitants")
  st.text("Settlement Size Category: 1 to 99 inhabitants")



with st.expander("Transport Availability", expanded= False):
  st.subheader("Public Transport")
  st.image("https://datasciencecampus.ons.gov.uk/wp-content/uploads/sites/10/2022/12/rear-view-of-grandfather-and-grandchildren-walking-2022-05-26-01-16-56-utc-1536x1024.jpg",width= 300)
  st.text("Bus: No")
  st.text("Taxi and colective transport: No")


with st.expander(
    "Governance, Social Aspects & Environment", expanded=False
):
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGrKaV0eiP6tiZKyJ2VAY0-bbJxBQem13sQWMwv8rEKA&s=10",width=300)
    st.subheader("Social Organization")
    st.text("Municipal Authority: Municipal Delegate")
    st.text("Ejido or Communal Property Commissioner: No")
    st.text("Local Police: No")


with st.expander("Economic Activities"):
  st.subheader("Economy")
  st.image("https://www.thoughtco.com/thmb/L7fRAc1rnIIDSL8nnD7lg6tNa6I=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-470554831-597bb30f9abed50010979aa0.jpg",width=300)
  st.text("Primary Production: Cattle raising & crop farming")
  st.text("Purpose: Mixed (Sale & family consumption)")
  st.text("Workplace Location: Within the locality")


with st.expander("Telecommunications & Connectivity"):
    st.subheader("Connectivity")
    st.image("https://definicion.de/wp-content/uploads/2008/05/telecomunicacion-1.jpg", width=300)
    st.text("Mobile Signal (Cellular): Available")
    st.text("Broadcast TV: Available")
    st.text("Public Internet & Phones: None")
    st.text("Pay TV & Financial Services: None")



with st.expander("Healthcare & Medical Services"):
    st.subheader("Healthcare Access")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSy3wpzGCT2GrRR_kLiofDUZ_Dthw3RJmqCADcLRXoVCQ&s=10",width=300)
    st.text("Local Medical Infrastructure: None (No clinics or private doctors)")
    st.text("Mobile / Outreach Health: None (No mobile health caravans or promoters)")
 

with st.expander("Community Dining & Food Support"):
    st.subheader("Community Food Access")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9qS7pbvgIhpHyxGLewVWaV91QG1PIBex8BHCWJhuJ8A&s=10",width=300)
    st.text("Dining Facilities: None (No state, municipal or community kitchens")
    st.text("Commercial Kitchens: None (No public dining services available)")


with st.expander("Local Commerce & Essential Supplies"):
  st.subheader("Essential Supplies")
  st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCdqqdAq33-Oo8pz3j2bquyvHPHCmsYRwVLm5b5yXhVg&s=10",width= 300)
  st.text("Grocery Stores: None ")
  st.text("Open-Air Markets: None ")
  st.text("Social Supply Stores (SEGALMEX-DICONSA / LICONSA): None")
  st.text("Pharmacy & Stationery: None")



with st.expander("Local Food Availability & Staples"):
  st.subheader("Food Access")
  st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcgJT1PMPV9-OyBtvlDy0sCCoEud3x1sE321t0Tu13Jw&s=10",width=300)
  st.text("Beans (Frijol): Available")
  st.text("Corn (Maíz): Available")
  st.text("Tortillas, Bread, Rice & Milk: None")
  st.text("Eggs, Beef, Pork, Chicken & Fresh Fish: None")
  st.text("Fruits & Vegetables: None")



with st.expander("Urban Infrastructure & Recreational Spaces"):
    st.subheader("Infraestructure")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRprr77RhlfBR8xhP9-HOhd0Vl9kg_g7aZhW69tpRdIw&s=10",width=300)
    st.text("Street Block Structure: None")
    st.text("Street Paving & Sidewalks: Not applicable")
    st.text("Public Plaza / Garden: None")
    st.text("Sports Court & Playground: None")
    st.text("Library, Cultural Center & Multipurpose Hall: None")


with st.expander("Public Lighting Infrastructure"):
  st.subheader("Lighting")
  st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTL-2YPTG367so4KqdRgl0DH4jooobf2QDiKyqSsxPuqg&s=10",width=300)
  st.text("Public Street Lighting: Available")
  st.text("Power Source: Federal Electricity Commission (CFE)")
  st.text("Coverage Area: Entire locality")



with st.expander("Drainage & Waste Management Services"):
  st.subheader("Drainage Access")
  st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSI8kSdZrm52JXOxPl-fscJ619p4Y7keHW2KMYx9XhWCQ&s=10",width= 300)
  st.text("Public Drainage Network: None")
  st.text("Public Area Street Sweeping / Cleaning: None")
  st.text("Household Trash Collection: Available")


with st.expander("Piped Water Supply"):
  st.subheader("Water Access")
  st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNHEfm_VoT7Cxq-dRLVWoaiy6_vvWORoVRvxH0oPGnZg&s=10",width=300)
  st.text("Water Distribution Network: Piped network")
  st.text("Coverage Area: Entire locality")
  st.text("Primary Water Source: Underground well (Pozo)")


with st.expander("References", expanded= False):
    st.subheader("Organizations")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRMd7EZp8RQ54Kx9hix91LVg5nLb_DGSyDFCC5e_XtSQ&s=10",width=300)
    st.write("INEGI: Censo de Población y Vivienda 2020 ")