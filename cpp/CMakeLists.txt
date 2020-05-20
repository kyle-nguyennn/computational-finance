cmake_minimum_required(VERSION 3.1)
project(PriceEngine)
set(CMAKE_CXX_STANDARD 17)
#set(CMAKE_VERBOSE_MAKEFILE ON)

##################################
# Download and install GoogleTest

include(ExternalProject)
ExternalProject_Add(gtest
  GIT_REPOSITORY https://github.com/google/googletest.git GIT_TAG release-1.8.1
  PREFIX ${CMAKE_CURRENT_BINARY_DIR}/gtest
  INSTALL_COMMAND ""
)
ExternalProject_Get_Property(gtest SOURCE_DIR BINARY_DIR)

message("Source dir of google test is: ${SOURCE_DIR}")
message("Source dir of google test is: ${BINARY_DIR}")
include_directories(${SOURCE_DIR}/googletest/include)
include_directories(${SOURCE_DIR}/googlemock/include)

######################
# add directories to include paths for compiler to search for header file
# include_directories(engine)

# add subdirectory to the build
# add_subdirectory(engine)
add_subdirectory(engine_tests)

# add output binary alias
add_executable(main main.cpp)

########################
###### Unit tests ######
########################
# Add test cpp file
add_executable(basic_check engine_tests/basic_check.cpp)
#####################################
###Configure the test to use GoogleTest

add_dependencies(basic_check gtest)
target_link_libraries(basic_check ${BINARY_DIR}/googlemock/gtest/libgtest.a)
target_link_libraries(basic_check ${BINARY_DIR}/googlemock/gtest/libgtest_main.a)

##################################
# Just make the test runnable with
#   $ make test

enable_testing()
add_test(NAME    basic_check 
         COMMAND basic_check)
