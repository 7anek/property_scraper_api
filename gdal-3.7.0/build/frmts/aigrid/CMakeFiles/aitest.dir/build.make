# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build

# Include any dependencies generated for this target.
include frmts/aigrid/CMakeFiles/aitest.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include frmts/aigrid/CMakeFiles/aitest.dir/compiler_depend.make

# Include the progress variables for this target.
include frmts/aigrid/CMakeFiles/aitest.dir/progress.make

# Include the compile flags for this target's objects.
include frmts/aigrid/CMakeFiles/aitest.dir/flags.make

frmts/aigrid/CMakeFiles/aitest.dir/aitest.c.o: frmts/aigrid/CMakeFiles/aitest.dir/flags.make
frmts/aigrid/CMakeFiles/aitest.dir/aitest.c.o: ../frmts/aigrid/aitest.c
frmts/aigrid/CMakeFiles/aitest.dir/aitest.c.o: frmts/aigrid/CMakeFiles/aitest.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object frmts/aigrid/CMakeFiles/aitest.dir/aitest.c.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/aigrid && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT frmts/aigrid/CMakeFiles/aitest.dir/aitest.c.o -MF CMakeFiles/aitest.dir/aitest.c.o.d -o CMakeFiles/aitest.dir/aitest.c.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/aigrid/aitest.c

frmts/aigrid/CMakeFiles/aitest.dir/aitest.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/aitest.dir/aitest.c.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/aigrid && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/aigrid/aitest.c > CMakeFiles/aitest.dir/aitest.c.i

frmts/aigrid/CMakeFiles/aitest.dir/aitest.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/aitest.dir/aitest.c.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/aigrid && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/aigrid/aitest.c -o CMakeFiles/aitest.dir/aitest.c.s

frmts/aigrid/CMakeFiles/aitest.dir/__/__/ogr/ogrpgeogeometry.cpp.o: frmts/aigrid/CMakeFiles/aitest.dir/flags.make
frmts/aigrid/CMakeFiles/aitest.dir/__/__/ogr/ogrpgeogeometry.cpp.o: ../ogr/ogrpgeogeometry.cpp
frmts/aigrid/CMakeFiles/aitest.dir/__/__/ogr/ogrpgeogeometry.cpp.o: frmts/aigrid/CMakeFiles/aitest.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object frmts/aigrid/CMakeFiles/aitest.dir/__/__/ogr/ogrpgeogeometry.cpp.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/aigrid && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT frmts/aigrid/CMakeFiles/aitest.dir/__/__/ogr/ogrpgeogeometry.cpp.o -MF CMakeFiles/aitest.dir/__/__/ogr/ogrpgeogeometry.cpp.o.d -o CMakeFiles/aitest.dir/__/__/ogr/ogrpgeogeometry.cpp.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/ogr/ogrpgeogeometry.cpp

frmts/aigrid/CMakeFiles/aitest.dir/__/__/ogr/ogrpgeogeometry.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/aitest.dir/__/__/ogr/ogrpgeogeometry.cpp.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/aigrid && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/ogr/ogrpgeogeometry.cpp > CMakeFiles/aitest.dir/__/__/ogr/ogrpgeogeometry.cpp.i

frmts/aigrid/CMakeFiles/aitest.dir/__/__/ogr/ogrpgeogeometry.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/aitest.dir/__/__/ogr/ogrpgeogeometry.cpp.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/aigrid && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/ogr/ogrpgeogeometry.cpp -o CMakeFiles/aitest.dir/__/__/ogr/ogrpgeogeometry.cpp.s

# Object files for target aitest
aitest_OBJECTS = \
"CMakeFiles/aitest.dir/aitest.c.o" \
"CMakeFiles/aitest.dir/__/__/ogr/ogrpgeogeometry.cpp.o"

# External object files for target aitest
aitest_EXTERNAL_OBJECTS = \
"/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/aigccitt.c.o" \
"/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/aigdataset.cpp.o" \
"/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/aigopen.c.o" \
"/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/gridlib.c.o" \
"/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/ogr/ogrsf_frmts/avc/CMakeFiles/ogr_AVC.dir/avc_bin.cpp.o" \
"/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/ogr/ogrsf_frmts/avc/CMakeFiles/ogr_AVC.dir/avc_rawbin.cpp.o" \
"/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/ogr/ogrsf_frmts/avc/CMakeFiles/ogr_AVC.dir/avc_e00gen.cpp.o" \
"/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/ogr/ogrsf_frmts/avc/CMakeFiles/ogr_AVC.dir/avc_e00parse.cpp.o" \
"/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/ogr/ogrsf_frmts/avc/CMakeFiles/ogr_AVC.dir/avc_e00read.cpp.o" \
"/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/ogr/ogrsf_frmts/avc/CMakeFiles/ogr_AVC.dir/avc_mbyte.cpp.o" \
"/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/ogr/ogrsf_frmts/avc/CMakeFiles/ogr_AVC.dir/avc_misc.cpp.o" \
"/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/ogr/ogrsf_frmts/avc/CMakeFiles/ogr_AVC.dir/ogravcbindatasource.cpp.o" \
"/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/ogr/ogrsf_frmts/avc/CMakeFiles/ogr_AVC.dir/ogravcbindriver.cpp.o" \
"/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/ogr/ogrsf_frmts/avc/CMakeFiles/ogr_AVC.dir/ogravcbinlayer.cpp.o" \
"/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/ogr/ogrsf_frmts/avc/CMakeFiles/ogr_AVC.dir/ogravce00datasource.cpp.o" \
"/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/ogr/ogrsf_frmts/avc/CMakeFiles/ogr_AVC.dir/ogravcdatasource.cpp.o" \
"/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/ogr/ogrsf_frmts/avc/CMakeFiles/ogr_AVC.dir/ogravce00driver.cpp.o" \
"/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/ogr/ogrsf_frmts/avc/CMakeFiles/ogr_AVC.dir/ogravce00layer.cpp.o" \
"/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/ogr/ogrsf_frmts/avc/CMakeFiles/ogr_AVC.dir/ogravclayer.cpp.o" \
"/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/ogr/ogrsf_frmts/shape/CMakeFiles/ogr_Shape.dir/shape2ogr.cpp.o" \
"/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/ogr/ogrsf_frmts/shape/CMakeFiles/ogr_Shape.dir/shp_vsi.c.o" \
"/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/ogr/ogrsf_frmts/shape/CMakeFiles/ogr_Shape.dir/ogrshapedatasource.cpp.o" \
"/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/ogr/ogrsf_frmts/shape/CMakeFiles/ogr_Shape.dir/ogrshapedriver.cpp.o" \
"/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/ogr/ogrsf_frmts/shape/CMakeFiles/ogr_Shape.dir/ogrshapelayer.cpp.o"

frmts/aigrid/aitest: frmts/aigrid/CMakeFiles/aitest.dir/aitest.c.o
frmts/aigrid/aitest: frmts/aigrid/CMakeFiles/aitest.dir/__/__/ogr/ogrpgeogeometry.cpp.o
frmts/aigrid/aitest: frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/aigccitt.c.o
frmts/aigrid/aitest: frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/aigdataset.cpp.o
frmts/aigrid/aitest: frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/aigopen.c.o
frmts/aigrid/aitest: frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/gridlib.c.o
frmts/aigrid/aitest: ogr/ogrsf_frmts/avc/CMakeFiles/ogr_AVC.dir/avc_bin.cpp.o
frmts/aigrid/aitest: ogr/ogrsf_frmts/avc/CMakeFiles/ogr_AVC.dir/avc_rawbin.cpp.o
frmts/aigrid/aitest: ogr/ogrsf_frmts/avc/CMakeFiles/ogr_AVC.dir/avc_e00gen.cpp.o
frmts/aigrid/aitest: ogr/ogrsf_frmts/avc/CMakeFiles/ogr_AVC.dir/avc_e00parse.cpp.o
frmts/aigrid/aitest: ogr/ogrsf_frmts/avc/CMakeFiles/ogr_AVC.dir/avc_e00read.cpp.o
frmts/aigrid/aitest: ogr/ogrsf_frmts/avc/CMakeFiles/ogr_AVC.dir/avc_mbyte.cpp.o
frmts/aigrid/aitest: ogr/ogrsf_frmts/avc/CMakeFiles/ogr_AVC.dir/avc_misc.cpp.o
frmts/aigrid/aitest: ogr/ogrsf_frmts/avc/CMakeFiles/ogr_AVC.dir/ogravcbindatasource.cpp.o
frmts/aigrid/aitest: ogr/ogrsf_frmts/avc/CMakeFiles/ogr_AVC.dir/ogravcbindriver.cpp.o
frmts/aigrid/aitest: ogr/ogrsf_frmts/avc/CMakeFiles/ogr_AVC.dir/ogravcbinlayer.cpp.o
frmts/aigrid/aitest: ogr/ogrsf_frmts/avc/CMakeFiles/ogr_AVC.dir/ogravce00datasource.cpp.o
frmts/aigrid/aitest: ogr/ogrsf_frmts/avc/CMakeFiles/ogr_AVC.dir/ogravcdatasource.cpp.o
frmts/aigrid/aitest: ogr/ogrsf_frmts/avc/CMakeFiles/ogr_AVC.dir/ogravce00driver.cpp.o
frmts/aigrid/aitest: ogr/ogrsf_frmts/avc/CMakeFiles/ogr_AVC.dir/ogravce00layer.cpp.o
frmts/aigrid/aitest: ogr/ogrsf_frmts/avc/CMakeFiles/ogr_AVC.dir/ogravclayer.cpp.o
frmts/aigrid/aitest: ogr/ogrsf_frmts/shape/CMakeFiles/ogr_Shape.dir/shape2ogr.cpp.o
frmts/aigrid/aitest: ogr/ogrsf_frmts/shape/CMakeFiles/ogr_Shape.dir/shp_vsi.c.o
frmts/aigrid/aitest: ogr/ogrsf_frmts/shape/CMakeFiles/ogr_Shape.dir/ogrshapedatasource.cpp.o
frmts/aigrid/aitest: ogr/ogrsf_frmts/shape/CMakeFiles/ogr_Shape.dir/ogrshapedriver.cpp.o
frmts/aigrid/aitest: ogr/ogrsf_frmts/shape/CMakeFiles/ogr_Shape.dir/ogrshapelayer.cpp.o
frmts/aigrid/aitest: frmts/aigrid/CMakeFiles/aitest.dir/build.make
frmts/aigrid/aitest: ogr/ogrsf_frmts/shape/CMakeFiles/shapelib.dir/sbnsearch_wrapper.c.o
frmts/aigrid/aitest: ogr/ogrsf_frmts/shape/CMakeFiles/shapelib.dir/shpopen_wrapper.c.o
frmts/aigrid/aitest: ogr/ogrsf_frmts/shape/CMakeFiles/shapelib.dir/shptree_wrapper.c.o
frmts/aigrid/aitest: ogr/ogrsf_frmts/shape/CMakeFiles/shapelib.dir/dbfopen_wrapper.c.o
frmts/aigrid/aitest: libgdal.so.33.3.7.0
frmts/aigrid/aitest: frmts/aigrid/CMakeFiles/aitest.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable aitest"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/aigrid && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/aitest.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
frmts/aigrid/CMakeFiles/aitest.dir/build: frmts/aigrid/aitest
.PHONY : frmts/aigrid/CMakeFiles/aitest.dir/build

frmts/aigrid/CMakeFiles/aitest.dir/clean:
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/aigrid && $(CMAKE_COMMAND) -P CMakeFiles/aitest.dir/cmake_clean.cmake
.PHONY : frmts/aigrid/CMakeFiles/aitest.dir/clean

frmts/aigrid/CMakeFiles/aitest.dir/depend:
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0 /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/aigrid /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/aigrid /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/aigrid/CMakeFiles/aitest.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : frmts/aigrid/CMakeFiles/aitest.dir/depend
