import argparse

from service.invitation_service import InvitationService

parser = argparse.ArgumentParser(description='This program returns a list of customers present with in a radius range')

parser.add_argument("-r", default=100.0,
                    help="Radius within which we want to invite customers in kms. Default value - 100.0", type=float)

parser.add_argument("-i", default="resources/customer.txt",
                    help="File for reading the input. Default value - resources/customer.txt",
                    type=str)

parser.add_argument("-o", default="resources/output.txt",
                    help="File for writing the output. Default value - resources/output.txt",
                    type=str)

args = parser.parse_args()

if not isinstance(args.r, float) \
        or args.r > 12742 or 0 >= args.r:
    raise ValueError("Invalid value for the radius - " + str(args.r) + " km")

invitation_service = InvitationService(args.i, args.o)
invitation_service.find_customers_within_radius(args.r)
print("Please check the output in " + args.o + " file.")
