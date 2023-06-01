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
include frmts/envisat/CMakeFiles/envisat_dump.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include frmts/envisat/CMakeFiles/envisat_dump.dir/compiler_depend.make

# Include the progress variables for this target.
include frmts/envisat/CMakeFiles/envisat_dump.dir/progress.make

# Include the compile flags for this target's objects.
include frmts/envisat/CMakeFiles/envisat_dump.dir/flags.make

frmts/envisat/CMakeFiles/envisat_dump.dir/envisat_dump.c.o: frmts/envisat/CMakeFiles/envisat_dump.dir/flags.make
frmts/envisat/CMakeFiles/envisat_dump.dir/envisat_dump.c.o: ../frmts/envisat/envisat_dump.c
frmts/envisat/CMakeFiles/envisat_dump.dir/envisat_dump.c.o: frmts/envisat/CMakeFiles/envisat_dump.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object frmts/envisat/CMakeFiles/envisat_dump.dir/envisat_dump.c.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/envisat && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT frmts/envisat/CMakeFiles/envisat_dump.dir/envisat_dump.c.o -MF CMakeFiles/envisat_dump.dir/envisat_dump.c.o.d -o CMakeFiles/envisat_dump.dir/envisat_dump.c.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/envisat/envisat_dump.c

frmts/envisat/CMakeFiles/envisat_dump.dir/envisat_dump.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/envisat_dump.dir/envisat_dump.c.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/envisat && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/envisat/envisat_dump.c > CMakeFiles/envisat_dump.dir/envisat_dump.c.i

frmts/envisat/CMakeFiles/envisat_dump.dir/envisat_dump.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/envisat_dump.dir/envisat_dump.c.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/envisat && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/envisat/envisat_dump.c -o CMakeFiles/envisat_dump.dir/envisat_dump.c.s

frmts/envisat/CMakeFiles/envisat_dump.dir/EnvisatFile.c.o: frmts/envisat/CMakeFiles/envisat_dump.dir/flags.make
frmts/envisat/CMakeFiles/envisat_dump.dir/EnvisatFile.c.o: ../frmts/envisat/EnvisatFile.c
frmts/envisat/CMakeFiles/envisat_dump.dir/EnvisatFile.c.o: frmts/envisat/CMakeFiles/envisat_dump.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object frmts/envisat/CMakeFiles/envisat_dump.dir/EnvisatFile.c.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/envisat && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT frmts/envisat/CMakeFiles/envisat_dump.dir/EnvisatFile.c.o -MF CMakeFiles/envisat_dump.dir/EnvisatFile.c.o.d -o CMakeFiles/envisat_dump.dir/EnvisatFile.c.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/envisat/EnvisatFile.c

frmts/envisat/CMakeFiles/envisat_dump.dir/EnvisatFile.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/envisat_dump.dir/EnvisatFile.c.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/envisat && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/envisat/EnvisatFile.c > CMakeFiles/envisat_dump.dir/EnvisatFile.c.i

frmts/envisat/CMakeFiles/envisat_dump.dir/EnvisatFile.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/envisat_dump.dir/EnvisatFile.c.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/envisat && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/envisat/EnvisatFile.c -o CMakeFiles/envisat_dump.dir/EnvisatFile.c.s

# Object files for target envisat_dump
envisat_dump_OBJECTS = \
"CMakeFiles/envisat_dump.dir/envisat_dump.c.o" \
"CMakeFiles/envisat_dump.dir/EnvisatFile.c.o"

# External object files for target envisat_dump
envisat_dump_EXTERNAL_OBJECTS =

frmts/envisat/envisat_dump: frmts/envisat/CMakeFiles/envisat_dump.dir/envisat_dump.c.o
frmts/envisat/envisat_dump: frmts/envisat/CMakeFiles/envisat_dump.dir/EnvisatFile.c.o
frmts/envisat/envisat_dump: frmts/envisat/CMakeFiles/envisat_dump.dir/build.make
frmts/envisat/envisat_dump: libgdal.so.33.3.7.0
frmts/envisat/envisat_dump: frmts/envisat/CMakeFiles/envisat_dump.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking C executable envisat_dump"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/envisat && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/envisat_dump.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
frmts/envisat/CMakeFiles/envisat_dump.dir/build: frmts/envisat/envisat_dump
.PHONY : frmts/envisat/CMakeFiles/envisat_dump.dir/build

frmts/envisat/CMakeFiles/envisat_dump.dir/clean:
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/envisat && $(CMAKE_COMMAND) -P CMakeFiles/envisat_dump.dir/cmake_clean.cmake
.PHONY : frmts/envisat/CMakeFiles/envisat_dump.dir/clean

frmts/envisat/CMakeFiles/envisat_dump.dir/depend:
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0 /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/envisat /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/envisat /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/envisat/CMakeFiles/envisat_dump.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : frmts/envisat/CMakeFiles/envisat_dump.dir/depend
