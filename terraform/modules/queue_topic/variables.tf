variable "region" {
  type        = string
  description = "The default region to use for AWS"
}

variable "queue_name" {
  type        = string
  description = "The name of the queue"
}

variable "topic_name" {
  type        = string
  description = "The name of the topic"
}
