from conan import ConanFile
from conan.tools.cmake import CMake
from conan.tools.scm import Git

class Test(ConanFile):
    name = "mytest"
    version = "0.1"
    generators = "CMakeToolchain"

    def export(self):
        git = Git(self, self.recipe_folder)
        scm_url, scm_commit = git.get_url_and_commit()
        update_conandata(self, {"sources": {"commit": scm_commit, "url": scm_url}})

    def source(self):
        git = Git(self)
        sources = self.conan_data["sources"]
        git.clone(url=sources["url"], target=".")
        git.checkout(commit=sources["commit"])
    
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
