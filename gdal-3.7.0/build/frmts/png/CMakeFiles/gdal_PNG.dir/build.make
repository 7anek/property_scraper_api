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
include frmts/png/CMakeFiles/gdal_PNG.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include frmts/png/CMakeFiles/gdal_PNG.dir/compiler_depend.make

# Include the progress variables for this target.
include frmts/png/CMakeFiles/gdal_PNG.dir/progress.make

# Include the compile flags for this target's objects.
include frmts/png/CMakeFiles/gdal_PNG.dir/flags.make

frmts/png/CMakeFiles/gdal_PNG.dir/pngdataset.cpp.o: frmts/png/CMakeFiles/gdal_PNG.dir/flags.make
frmts/png/CMakeFiles/gdal_PNG.dir/pngdataset.cpp.o: ../frmts/png/pngdataset.cpp
frmts/png/CMakeFiles/gdal_PNG.dir/pngdataset.cpp.o: frmts/png/CMakeFiles/gdal_PNG.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object frmts/png/CMakeFiles/gdal_PNG.dir/pngdataset.cpp.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/png && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT frmts/png/CMakeFiles/gdal_PNG.dir/pngdataset.cpp.o -MF CMakeFiles/gdal_PNG.dir/pngdataset.cpp.o.d -o CMakeFiles/gdal_PNG.dir/pngdataset.cpp.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/png/pngdataset.cpp

frmts/png/CMakeFiles/gdal_PNG.dir/pngdataset.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gdal_PNG.dir/pngdataset.cpp.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/png && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/png/pngdataset.cpp > CMakeFiles/gdal_PNG.dir/pngdataset.cpp.i

frmts/png/CMakeFiles/gdal_PNG.dir/pngdataset.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gdal_PNG.dir/pngdataset.cpp.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/png && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/png/pngdataset.cpp -o CMakeFiles/gdal_PNG.dir/pngdataset.cpp.s

gdal_PNG: frmts/png/CMakeFiles/gdal_PNG.dir/pngdataset.cpp.o
gdal_PNG: frmts/png/CMakeFiles/gdal_PNG.dir/build.make
.PHONY : gdal_PNG

# Rule to build all files generated by this target.
frmts/png/CMakeFiles/gdal_PNG.dir/build: gdal_PNG
.PHONY : frmts/png/CMakeFiles/gdal_PNG.dir/build

frmts/png/CMakeFiles/gdal_PNG.dir/clean:
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/png && $(CMAKE_COMMAND) -P CMakeFiles/gdal_PNG.dir/cmake_clean.cmake
.PHONY : frmts/png/CMakeFiles/gdal_PNG.dir/clean

frmts/png/CMakeFiles/gdal_PNG.dir/depend:
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0 /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/png /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/png /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/png/CMakeFiles/gdal_PNG.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : frmts/png/CMakeFiles/gdal_PNG.dir/depend
