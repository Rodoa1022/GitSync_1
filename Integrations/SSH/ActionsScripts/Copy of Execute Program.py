from SiemplifyUtils import output_handler
from SiemplifyDataModel import EntityTypes
from SiemplifyAction import *
from SshManager import SshManager
import subprocess


@output_handler
def main():
    siemplify = SiemplifyAction()
    # Command to execute
    cmd = ["ps", "-ef"]

    # Execute the command

    subprocess.run(["ls", "-l"]) 

    #status_code, output, error = ssh_wrapper.execute_program(siemplify.parameters['Remote Program Path'])
    #if status_code == 0:
    #    results = 'True'
    #    output_message = output.read()
    #else:
    #    results = 'False'
    #    output_message = error.read()
    #siemplify.end(output_message, results)


if __name__ == "__main__":
    main()