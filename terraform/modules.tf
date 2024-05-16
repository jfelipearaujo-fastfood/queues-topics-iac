module "order_payment" {
  source = "./modules/queue_topic"

  region = var.region

  queue_name = "OrderPaymentQueue"
  topic_name = "OrderPaymentTopic"
}

module "update_order" {
  source = "./modules/queue_topic"

  region = var.region

  queue_name = "UpdateOrderQueue"
  topic_name = "UpdateOrderTopic"
}

module "order_production" {
  source = "./modules/queue_topic"

  region = var.region

  queue_name = "OrderProductionQueue"
  topic_name = "OrderProductionTopic"
}
