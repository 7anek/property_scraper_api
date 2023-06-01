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
include frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/compiler_depend.make

# Include the progress variables for this target.
include frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/progress.make

# Include the compile flags for this target's objects.
include frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/flags.make

frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/aigccitt.c.o: frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/flags.make
frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/aigccitt.c.o: ../frmts/aigrid/aigccitt.c
frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/aigccitt.c.o: frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/aigccitt.c.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/aigrid && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/aigccitt.c.o -MF CMakeFiles/gdal_AIGrid.dir/aigccitt.c.o.d -o CMakeFiles/gdal_AIGrid.dir/aigccitt.c.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/aigrid/aigccitt.c

frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/aigccitt.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/gdal_AIGrid.dir/aigccitt.c.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/aigrid && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/aigrid/aigccitt.c > CMakeFiles/gdal_AIGrid.dir/aigccitt.c.i

frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/aigccitt.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/gdal_AIGrid.dir/aigccitt.c.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/aigrid && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/aigrid/aigccitt.c -o CMakeFiles/gdal_AIGrid.dir/aigccitt.c.s

frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/aigdataset.cpp.o: frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/flags.make
frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/aigdataset.cpp.o: ../frmts/aigrid/aigdataset.cpp
frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/aigdataset.cpp.o: frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/aigdataset.cpp.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/aigrid && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/aigdataset.cpp.o -MF CMakeFiles/gdal_AIGrid.dir/aigdataset.cpp.o.d -o CMakeFiles/gdal_AIGrid.dir/aigdataset.cpp.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/aigrid/aigdataset.cpp

frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/aigdataset.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gdal_AIGrid.dir/aigdataset.cpp.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/aigrid && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/aigrid/aigdataset.cpp > CMakeFiles/gdal_AIGrid.dir/aigdataset.cpp.i

frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/aigdataset.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gdal_AIGrid.dir/aigdataset.cpp.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/aigrid && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/aigrid/aigdataset.cpp -o CMakeFiles/gdal_AIGrid.dir/aigdataset.cpp.s

frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/aigopen.c.o: frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/flags.make
frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/aigopen.c.o: ../frmts/aigrid/aigopen.c
frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/aigopen.c.o: frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building C object frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/aigopen.c.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/aigrid && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/aigopen.c.o -MF CMakeFiles/gdal_AIGrid.dir/aigopen.c.o.d -o CMakeFiles/gdal_AIGrid.dir/aigopen.c.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/aigrid/aigopen.c

frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/aigopen.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/gdal_AIGrid.dir/aigopen.c.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/aigrid && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/aigrid/aigopen.c > CMakeFiles/gdal_AIGrid.dir/aigopen.c.i

frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/aigopen.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/gdal_AIGrid.dir/aigopen.c.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/aigrid && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/aigrid/aigopen.c -o CMakeFiles/gdal_AIGrid.dir/aigopen.c.s

frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/gridlib.c.o: frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/flags.make
frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/gridlib.c.o: ../frmts/aigrid/gridlib.c
frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/gridlib.c.o: frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building C object frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/gridlib.c.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/aigrid && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/gridlib.c.o -MF CMakeFiles/gdal_AIGrid.dir/gridlib.c.o.d -o CMakeFiles/gdal_AIGrid.dir/gridlib.c.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/aigrid/gridlib.c

frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/gridlib.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/gdal_AIGrid.dir/gridlib.c.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/aigrid && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/aigrid/gridlib.c > CMakeFiles/gdal_AIGrid.dir/gridlib.c.i

frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/gridlib.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/gdal_AIGrid.dir/gridlib.c.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/aigrid && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/aigrid/gridlib.c -o CMakeFiles/gdal_AIGrid.dir/gridlib.c.s

gdal_AIGrid: frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/aigccitt.c.o
gdal_AIGrid: frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/aigdataset.cpp.o
gdal_AIGrid: frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/aigopen.c.o
gdal_AIGrid: frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/gridlib.c.o
gdal_AIGrid: frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/build.make
.PHONY : gdal_AIGrid

# Rule to build all files generated by this target.
frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/build: gdal_AIGrid
.PHONY : frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/build

frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/clean:
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/aigrid && $(CMAKE_COMMAND) -P CMakeFiles/gdal_AIGrid.dir/cmake_clean.cmake
.PHONY : frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/clean

frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/depend:
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0 /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/aigrid /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/aigrid /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : frmts/aigrid/CMakeFiles/gdal_AIGrid.dir/depend
