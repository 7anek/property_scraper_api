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
include frmts/pds/CMakeFiles/gdal_PDS.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include frmts/pds/CMakeFiles/gdal_PDS.dir/compiler_depend.make

# Include the progress variables for this target.
include frmts/pds/CMakeFiles/gdal_PDS.dir/progress.make

# Include the compile flags for this target's objects.
include frmts/pds/CMakeFiles/gdal_PDS.dir/flags.make

frmts/pds/CMakeFiles/gdal_PDS.dir/isis2dataset.cpp.o: frmts/pds/CMakeFiles/gdal_PDS.dir/flags.make
frmts/pds/CMakeFiles/gdal_PDS.dir/isis2dataset.cpp.o: ../frmts/pds/isis2dataset.cpp
frmts/pds/CMakeFiles/gdal_PDS.dir/isis2dataset.cpp.o: frmts/pds/CMakeFiles/gdal_PDS.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object frmts/pds/CMakeFiles/gdal_PDS.dir/isis2dataset.cpp.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/pds && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT frmts/pds/CMakeFiles/gdal_PDS.dir/isis2dataset.cpp.o -MF CMakeFiles/gdal_PDS.dir/isis2dataset.cpp.o.d -o CMakeFiles/gdal_PDS.dir/isis2dataset.cpp.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/pds/isis2dataset.cpp

frmts/pds/CMakeFiles/gdal_PDS.dir/isis2dataset.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gdal_PDS.dir/isis2dataset.cpp.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/pds && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/pds/isis2dataset.cpp > CMakeFiles/gdal_PDS.dir/isis2dataset.cpp.i

frmts/pds/CMakeFiles/gdal_PDS.dir/isis2dataset.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gdal_PDS.dir/isis2dataset.cpp.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/pds && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/pds/isis2dataset.cpp -o CMakeFiles/gdal_PDS.dir/isis2dataset.cpp.s

frmts/pds/CMakeFiles/gdal_PDS.dir/isis3dataset.cpp.o: frmts/pds/CMakeFiles/gdal_PDS.dir/flags.make
frmts/pds/CMakeFiles/gdal_PDS.dir/isis3dataset.cpp.o: ../frmts/pds/isis3dataset.cpp
frmts/pds/CMakeFiles/gdal_PDS.dir/isis3dataset.cpp.o: frmts/pds/CMakeFiles/gdal_PDS.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object frmts/pds/CMakeFiles/gdal_PDS.dir/isis3dataset.cpp.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/pds && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT frmts/pds/CMakeFiles/gdal_PDS.dir/isis3dataset.cpp.o -MF CMakeFiles/gdal_PDS.dir/isis3dataset.cpp.o.d -o CMakeFiles/gdal_PDS.dir/isis3dataset.cpp.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/pds/isis3dataset.cpp

frmts/pds/CMakeFiles/gdal_PDS.dir/isis3dataset.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gdal_PDS.dir/isis3dataset.cpp.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/pds && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/pds/isis3dataset.cpp > CMakeFiles/gdal_PDS.dir/isis3dataset.cpp.i

frmts/pds/CMakeFiles/gdal_PDS.dir/isis3dataset.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gdal_PDS.dir/isis3dataset.cpp.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/pds && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/pds/isis3dataset.cpp -o CMakeFiles/gdal_PDS.dir/isis3dataset.cpp.s

frmts/pds/CMakeFiles/gdal_PDS.dir/pdsdataset.cpp.o: frmts/pds/CMakeFiles/gdal_PDS.dir/flags.make
frmts/pds/CMakeFiles/gdal_PDS.dir/pdsdataset.cpp.o: ../frmts/pds/pdsdataset.cpp
frmts/pds/CMakeFiles/gdal_PDS.dir/pdsdataset.cpp.o: frmts/pds/CMakeFiles/gdal_PDS.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object frmts/pds/CMakeFiles/gdal_PDS.dir/pdsdataset.cpp.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/pds && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT frmts/pds/CMakeFiles/gdal_PDS.dir/pdsdataset.cpp.o -MF CMakeFiles/gdal_PDS.dir/pdsdataset.cpp.o.d -o CMakeFiles/gdal_PDS.dir/pdsdataset.cpp.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/pds/pdsdataset.cpp

frmts/pds/CMakeFiles/gdal_PDS.dir/pdsdataset.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gdal_PDS.dir/pdsdataset.cpp.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/pds && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/pds/pdsdataset.cpp > CMakeFiles/gdal_PDS.dir/pdsdataset.cpp.i

frmts/pds/CMakeFiles/gdal_PDS.dir/pdsdataset.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gdal_PDS.dir/pdsdataset.cpp.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/pds && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/pds/pdsdataset.cpp -o CMakeFiles/gdal_PDS.dir/pdsdataset.cpp.s

frmts/pds/CMakeFiles/gdal_PDS.dir/pds4dataset.cpp.o: frmts/pds/CMakeFiles/gdal_PDS.dir/flags.make
frmts/pds/CMakeFiles/gdal_PDS.dir/pds4dataset.cpp.o: ../frmts/pds/pds4dataset.cpp
frmts/pds/CMakeFiles/gdal_PDS.dir/pds4dataset.cpp.o: frmts/pds/CMakeFiles/gdal_PDS.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object frmts/pds/CMakeFiles/gdal_PDS.dir/pds4dataset.cpp.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/pds && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT frmts/pds/CMakeFiles/gdal_PDS.dir/pds4dataset.cpp.o -MF CMakeFiles/gdal_PDS.dir/pds4dataset.cpp.o.d -o CMakeFiles/gdal_PDS.dir/pds4dataset.cpp.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/pds/pds4dataset.cpp

frmts/pds/CMakeFiles/gdal_PDS.dir/pds4dataset.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gdal_PDS.dir/pds4dataset.cpp.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/pds && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/pds/pds4dataset.cpp > CMakeFiles/gdal_PDS.dir/pds4dataset.cpp.i

frmts/pds/CMakeFiles/gdal_PDS.dir/pds4dataset.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gdal_PDS.dir/pds4dataset.cpp.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/pds && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/pds/pds4dataset.cpp -o CMakeFiles/gdal_PDS.dir/pds4dataset.cpp.s

frmts/pds/CMakeFiles/gdal_PDS.dir/pds4vector.cpp.o: frmts/pds/CMakeFiles/gdal_PDS.dir/flags.make
frmts/pds/CMakeFiles/gdal_PDS.dir/pds4vector.cpp.o: ../frmts/pds/pds4vector.cpp
frmts/pds/CMakeFiles/gdal_PDS.dir/pds4vector.cpp.o: frmts/pds/CMakeFiles/gdal_PDS.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building CXX object frmts/pds/CMakeFiles/gdal_PDS.dir/pds4vector.cpp.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/pds && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT frmts/pds/CMakeFiles/gdal_PDS.dir/pds4vector.cpp.o -MF CMakeFiles/gdal_PDS.dir/pds4vector.cpp.o.d -o CMakeFiles/gdal_PDS.dir/pds4vector.cpp.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/pds/pds4vector.cpp

frmts/pds/CMakeFiles/gdal_PDS.dir/pds4vector.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gdal_PDS.dir/pds4vector.cpp.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/pds && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/pds/pds4vector.cpp > CMakeFiles/gdal_PDS.dir/pds4vector.cpp.i

frmts/pds/CMakeFiles/gdal_PDS.dir/pds4vector.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gdal_PDS.dir/pds4vector.cpp.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/pds && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/pds/pds4vector.cpp -o CMakeFiles/gdal_PDS.dir/pds4vector.cpp.s

frmts/pds/CMakeFiles/gdal_PDS.dir/vicardataset.cpp.o: frmts/pds/CMakeFiles/gdal_PDS.dir/flags.make
frmts/pds/CMakeFiles/gdal_PDS.dir/vicardataset.cpp.o: ../frmts/pds/vicardataset.cpp
frmts/pds/CMakeFiles/gdal_PDS.dir/vicardataset.cpp.o: frmts/pds/CMakeFiles/gdal_PDS.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Building CXX object frmts/pds/CMakeFiles/gdal_PDS.dir/vicardataset.cpp.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/pds && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT frmts/pds/CMakeFiles/gdal_PDS.dir/vicardataset.cpp.o -MF CMakeFiles/gdal_PDS.dir/vicardataset.cpp.o.d -o CMakeFiles/gdal_PDS.dir/vicardataset.cpp.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/pds/vicardataset.cpp

frmts/pds/CMakeFiles/gdal_PDS.dir/vicardataset.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gdal_PDS.dir/vicardataset.cpp.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/pds && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/pds/vicardataset.cpp > CMakeFiles/gdal_PDS.dir/vicardataset.cpp.i

frmts/pds/CMakeFiles/gdal_PDS.dir/vicardataset.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gdal_PDS.dir/vicardataset.cpp.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/pds && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/pds/vicardataset.cpp -o CMakeFiles/gdal_PDS.dir/vicardataset.cpp.s

frmts/pds/CMakeFiles/gdal_PDS.dir/vicarkeywordhandler.cpp.o: frmts/pds/CMakeFiles/gdal_PDS.dir/flags.make
frmts/pds/CMakeFiles/gdal_PDS.dir/vicarkeywordhandler.cpp.o: ../frmts/pds/vicarkeywordhandler.cpp
frmts/pds/CMakeFiles/gdal_PDS.dir/vicarkeywordhandler.cpp.o: frmts/pds/CMakeFiles/gdal_PDS.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "Building CXX object frmts/pds/CMakeFiles/gdal_PDS.dir/vicarkeywordhandler.cpp.o"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/pds && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT frmts/pds/CMakeFiles/gdal_PDS.dir/vicarkeywordhandler.cpp.o -MF CMakeFiles/gdal_PDS.dir/vicarkeywordhandler.cpp.o.d -o CMakeFiles/gdal_PDS.dir/vicarkeywordhandler.cpp.o -c /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/pds/vicarkeywordhandler.cpp

frmts/pds/CMakeFiles/gdal_PDS.dir/vicarkeywordhandler.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gdal_PDS.dir/vicarkeywordhandler.cpp.i"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/pds && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/pds/vicarkeywordhandler.cpp > CMakeFiles/gdal_PDS.dir/vicarkeywordhandler.cpp.i

frmts/pds/CMakeFiles/gdal_PDS.dir/vicarkeywordhandler.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gdal_PDS.dir/vicarkeywordhandler.cpp.s"
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/pds && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/pds/vicarkeywordhandler.cpp -o CMakeFiles/gdal_PDS.dir/vicarkeywordhandler.cpp.s

gdal_PDS: frmts/pds/CMakeFiles/gdal_PDS.dir/isis2dataset.cpp.o
gdal_PDS: frmts/pds/CMakeFiles/gdal_PDS.dir/isis3dataset.cpp.o
gdal_PDS: frmts/pds/CMakeFiles/gdal_PDS.dir/pdsdataset.cpp.o
gdal_PDS: frmts/pds/CMakeFiles/gdal_PDS.dir/pds4dataset.cpp.o
gdal_PDS: frmts/pds/CMakeFiles/gdal_PDS.dir/pds4vector.cpp.o
gdal_PDS: frmts/pds/CMakeFiles/gdal_PDS.dir/vicardataset.cpp.o
gdal_PDS: frmts/pds/CMakeFiles/gdal_PDS.dir/vicarkeywordhandler.cpp.o
gdal_PDS: frmts/pds/CMakeFiles/gdal_PDS.dir/build.make
.PHONY : gdal_PDS

# Rule to build all files generated by this target.
frmts/pds/CMakeFiles/gdal_PDS.dir/build: gdal_PDS
.PHONY : frmts/pds/CMakeFiles/gdal_PDS.dir/build

frmts/pds/CMakeFiles/gdal_PDS.dir/clean:
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/pds && $(CMAKE_COMMAND) -P CMakeFiles/gdal_PDS.dir/cmake_clean.cmake
.PHONY : frmts/pds/CMakeFiles/gdal_PDS.dir/clean

frmts/pds/CMakeFiles/gdal_PDS.dir/depend:
	cd /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0 /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/frmts/pds /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/pds /home/janek/PycharmProjects/property_scraper_api/gdal-3.7.0/build/frmts/pds/CMakeFiles/gdal_PDS.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : frmts/pds/CMakeFiles/gdal_PDS.dir/depend
