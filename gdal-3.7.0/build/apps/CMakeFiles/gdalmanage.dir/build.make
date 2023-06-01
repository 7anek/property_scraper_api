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
include apps/CMakeFiles/gdalmanage.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include apps/CMakeFiles/gdalmanage.dir/compiler_depend.make

# Include the progress variables for this target.
include apps/CMakeFiles/gdalmanage.dir/progress.make

# Include the compile flags for this target's objects.
include apps/CMakeFiles/gdalmanage.dir/flags.make

apps/CMakeFiles/gdalmanage.dir/gdalmanage.cpp.o: apps/CMakeFiles/gdalmanage.dir/flags.make
apps/CMakeFiles/gdalmanage.dir/gdalmanage.cpp.o: ../apps/gdalmanage.cpp
apps/CMakeFiles/gdalmanage.dir/gdalmanage.cpp.o: apps/CMakeFiles/gdalmanage.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object apps/CMakeFiles/gdalmanage.dir/gdalmanage.cpp.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT apps/CMakeFiles/gdalmanage.dir/gdalmanage.cpp.o -MF CMakeFiles/gdalmanage.dir/gdalmanage.cpp.o.d -o CMakeFiles/gdalmanage.dir/gdalmanage.cpp.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdalmanage.cpp

apps/CMakeFiles/gdalmanage.dir/gdalmanage.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gdalmanage.dir/gdalmanage.cpp.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdalmanage.cpp > CMakeFiles/gdalmanage.dir/gdalmanage.cpp.i

apps/CMakeFiles/gdalmanage.dir/gdalmanage.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gdalmanage.dir/gdalmanage.cpp.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdalmanage.cpp -o CMakeFiles/gdalmanage.dir/gdalmanage.cpp.s

# Object files for target gdalmanage
gdalmanage_OBJECTS = \
"CMakeFiles/gdalmanage.dir/gdalmanage.cpp.o"

# External object files for target gdalmanage
gdalmanage_EXTERNAL_OBJECTS =

apps/gdalmanage: apps/CMakeFiles/gdalmanage.dir/gdalmanage.cpp.o
apps/gdalmanage: apps/CMakeFiles/gdalmanage.dir/build.make
apps/gdalmanage: libgdal.so.33.3.7.0
apps/gdalmanage: apps/CMakeFiles/gdalmanage.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable gdalmanage"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/gdalmanage.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
apps/CMakeFiles/gdalmanage.dir/build: apps/gdalmanage
.PHONY : apps/CMakeFiles/gdalmanage.dir/build

apps/CMakeFiles/gdalmanage.dir/clean:
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && $(CMAKE_COMMAND) -P CMakeFiles/gdalmanage.dir/cmake_clean.cmake
.PHONY : apps/CMakeFiles/gdalmanage.dir/clean

apps/CMakeFiles/gdalmanage.dir/depend:
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0 /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps/CMakeFiles/gdalmanage.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : apps/CMakeFiles/gdalmanage.dir/depend
