terraform {
 /* backend "s3" {
      bucket = "terraform-tfstate-saitejaa"
   }*/
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = ">= 0.11.0"
    }
  }
}


provider "aws" {
  profile = "tek"
  region  = var.region
}

