provider "aws" {
  region                  = "ap-south-1"
  profile                 = "terraform"
}

resource "aws_instance" "web" {
  ami			= "ami-010aff33ed5991201"
  instance_type		= "t2.micro"
  tags = {
    Name = "Web Server"
  }
  security_groups 	= [ "launch-wizard-1" ]
  key_name = "OSkey"
}

resource "aws_ebs_volume" "storae" {
  availability_zone = "ap-south-1a"
  size              = 5

  tags = {
    Name = "storage OF 5 gb"
  }
}