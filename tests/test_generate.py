from pprint import pprint

from cloudmesh_base.util import HEADING
from cloudmesh_base.util import banner

from cloudmesh_management.project import Project
from cloudmesh_management.generate import generate_users
from cloudmesh_management.generate import generate_projects


class TestGenerate:
 
    def setup(self):
        # HEADING()
        pass
    
    def teardown(self):
        # HEADING()
        pass

    def test_generate(self):
        HEADING()

        generate_users(10)
        # generate_projects(3)
        #
        # banner("Find")
        # #print users.find()
        # banner("Find [0]")
        # #print users.find()[0]
        #
        # projects = Project.objects()
        # print projects.count()
        # pprint (projects[0])


