resource "aws_s3_bucket" "trivy_reports" {
  bucket = "${var.project_name}-trivy-reports"

  tags = {
    Name = "${var.project_name}-trivy-reports"
  }
}

resource "aws_s3_bucket_versioning" "trivy_reports" {
  bucket = aws_s3_bucket.trivy_reports.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "trivy_reports" {
  bucket = aws_s3_bucket.trivy_reports.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "trivy_reports" {
  bucket = aws_s3_bucket.trivy_reports.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_lifecycle_configuration" "trivy_reports" {
  bucket = aws_s3_bucket.trivy_reports.id

  rule {
    id     = "expire-old-reports"
    status = "Enabled"

    expiration {
      days = 90
    }
  }
}