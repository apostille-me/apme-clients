cmake_minimum_required(VERSION 3.16)
project(apme_client_cpp VERSION 0.1.0 LANGUAGES CXX)

add_library(apme_client_cpp STATIC src/client.cpp)
target_include_directories(apme_client_cpp PUBLIC include)
target_compile_features(apme_client_cpp PUBLIC cxx_std_17)

include(CTest)
if(BUILD_TESTING)
  add_executable(apme_client_cpp_test tests/client_test.cpp)
  target_link_libraries(apme_client_cpp_test PRIVATE apme_client_cpp)
  add_test(NAME apme_client_cpp_test COMMAND apme_client_cpp_test)
endif()
