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
include frmts/daas/CMakeFiles/gdal_DAAS.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include frmts/daas/CMakeFiles/gdal_DAAS.dir/compiler_depend.make

# Include the progress variables for this target.
include frmts/daas/CMakeFiles/gdal_DAAS.dir/progress.make

# Include the compile flags for this target's objects.
include frmts/daas/CMakeFiles/gdal_DAAS.dir/flags.make

frmts/daas/CMakeFiles/gdal_DAAS.dir/daasdataset.cpp.o: frmts/daas/CMakeFiles/gdal_DAAS.dir/flags.make
frmts/daas/CMakeFiles/gdal_DAAS.dir/daasdataset.cpp.o: ../frmts/daas/daasdataset.cpp
frmts/daas/CMakeFiles/gdal_DAAS.dir/daasdataset.cpp.o: frmts/daas/CMakeFiles/gdal_DAAS.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object frmts/daas/CMakeFiles/gdal_DAAS.dir/daasdataset.cpp.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/daas && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT frmts/daas/CMakeFiles/gdal_DAAS.dir/daasdataset.cpp.o -MF CMakeFiles/gdal_DAAS.dir/daasdataset.cpp.o.d -o CMakeFiles/gdal_DAAS.dir/daasdataset.cpp.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/daas/daasdataset.cpp

frmts/daas/CMakeFiles/gdal_DAAS.dir/daasdataset.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gdal_DAAS.dir/daasdataset.cpp.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/daas && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/daas/daasdataset.cpp > CMakeFiles/gdal_DAAS.dir/daasdataset.cpp.i

frmts/daas/CMakeFiles/gdal_DAAS.dir/daasdataset.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gdal_DAAS.dir/daasdataset.cpp.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/daas && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/daas/daasdataset.cpp -o CMakeFiles/gdal_DAAS.dir/daasdataset.cpp.s

gdal_DAAS: frmts/daas/CMakeFiles/gdal_DAAS.dir/daasdataset.cpp.o
gdal_DAAS: frmts/daas/CMakeFiles/gdal_DAAS.dir/build.make
.PHONY : gdal_DAAS

# Rule to build all files generated by this target.
frmts/daas/CMakeFiles/gdal_DAAS.dir/build: gdal_DAAS
.PHONY : frmts/daas/CMakeFiles/gdal_DAAS.dir/build

frmts/daas/CMakeFiles/gdal_DAAS.dir/clean:
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/daas && $(CMAKE_COMMAND) -P CMakeFiles/gdal_DAAS.dir/cmake_clean.cmake
.PHONY : frmts/daas/CMakeFiles/gdal_DAAS.dir/clean

frmts/daas/CMakeFiles/gdal_DAAS.dir/depend:
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0 /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/daas /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/daas /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/daas/CMakeFiles/gdal_DAAS.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : frmts/daas/CMakeFiles/gdal_DAAS.dir/depend
