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
include apps/CMakeFiles/gdalflattenmask.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include apps/CMakeFiles/gdalflattenmask.dir/compiler_depend.make

# Include the progress variables for this target.
include apps/CMakeFiles/gdalflattenmask.dir/progress.make

# Include the compile flags for this target's objects.
include apps/CMakeFiles/gdalflattenmask.dir/flags.make

apps/CMakeFiles/gdalflattenmask.dir/gdalflattenmask.c.o: apps/CMakeFiles/gdalflattenmask.dir/flags.make
apps/CMakeFiles/gdalflattenmask.dir/gdalflattenmask.c.o: ../apps/gdalflattenmask.c
apps/CMakeFiles/gdalflattenmask.dir/gdalflattenmask.c.o: apps/CMakeFiles/gdalflattenmask.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object apps/CMakeFiles/gdalflattenmask.dir/gdalflattenmask.c.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT apps/CMakeFiles/gdalflattenmask.dir/gdalflattenmask.c.o -MF CMakeFiles/gdalflattenmask.dir/gdalflattenmask.c.o.d -o CMakeFiles/gdalflattenmask.dir/gdalflattenmask.c.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdalflattenmask.c

apps/CMakeFiles/gdalflattenmask.dir/gdalflattenmask.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/gdalflattenmask.dir/gdalflattenmask.c.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdalflattenmask.c > CMakeFiles/gdalflattenmask.dir/gdalflattenmask.c.i

apps/CMakeFiles/gdalflattenmask.dir/gdalflattenmask.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/gdalflattenmask.dir/gdalflattenmask.c.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps/gdalflattenmask.c -o CMakeFiles/gdalflattenmask.dir/gdalflattenmask.c.s

# Object files for target gdalflattenmask
gdalflattenmask_OBJECTS = \
"CMakeFiles/gdalflattenmask.dir/gdalflattenmask.c.o"

# External object files for target gdalflattenmask
gdalflattenmask_EXTERNAL_OBJECTS =

apps/gdalflattenmask: apps/CMakeFiles/gdalflattenmask.dir/gdalflattenmask.c.o
apps/gdalflattenmask: apps/CMakeFiles/gdalflattenmask.dir/build.make
apps/gdalflattenmask: libgdal.so.33.3.7.0
apps/gdalflattenmask: apps/CMakeFiles/gdalflattenmask.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable gdalflattenmask"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/gdalflattenmask.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
apps/CMakeFiles/gdalflattenmask.dir/build: apps/gdalflattenmask
.PHONY : apps/CMakeFiles/gdalflattenmask.dir/build

apps/CMakeFiles/gdalflattenmask.dir/clean:
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps && $(CMAKE_COMMAND) -P CMakeFiles/gdalflattenmask.dir/cmake_clean.cmake
.PHONY : apps/CMakeFiles/gdalflattenmask.dir/clean

apps/CMakeFiles/gdalflattenmask.dir/depend:
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0 /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/apps /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/apps/CMakeFiles/gdalflattenmask.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : apps/CMakeFiles/gdalflattenmask.dir/depend
