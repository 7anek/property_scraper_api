file(REMOVE_RECURSE
  "libgdal.pdb"
  "libgdal.so"
  "libgdal.so.33"
  "libgdal.so.33.3.7.0"
)

# Per-language clean rules from dependency scanning.
foreach(lang C CXX)
  include(CMakeFiles/GDAL.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()
