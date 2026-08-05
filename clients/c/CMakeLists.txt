cmake_minimum_required(VERSION 3.16)
project(apme_client_c VERSION 0.1.0 LANGUAGES C)

add_library(apme_client_c STATIC src/client.c)
target_include_directories(apme_client_c PUBLIC include)
target_compile_features(apme_client_c PUBLIC c_std_11)

include(CTest)
if(BUILD_TESTING)
  add_executable(apme_client_c_test tests/client_test.c)
  target_link_libraries(apme_client_c_test PRIVATE apme_client_c)
  add_test(NAME apme_client_c_test COMMAND apme_client_c_test)
endif()
