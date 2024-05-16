from diagrams import Cluster, Diagram
from diagrams.aws.integration import SimpleQueueServiceSqs as SQS
from diagrams.aws.integration import SimpleNotificationServiceSns as SNS

diagram_attr = {
    "fontsize": "25",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "spline",
}

node_attr = {
    "fontsize": "20",
    "size": "6",
    "bgcolor": "white",
    "margin": "1",
    "height": "3",
    "pad": "5"
}

cluster_attr = {
    "fontsize": "20",
    "size": "5",
    "margin": "28",
    "pad": "3"
}

item_attr = {
    "fontsize": "20",
    "height": "2.2"
}

def sns_sqs_link(sns_name, sqs_name):
    sns = SNS(sns_name)
    sqs = SQS(sqs_name)

    sns >> sqs

with Diagram("Cloud AWS Queues Topics", show=False, graph_attr=diagram_attr):    
    with Cluster("AWS", graph_attr=cluster_attr):
        sns_sqs_link("OrderPaymentTopic", "OrderPaymentQueue")
        sns_sqs_link("UpdateOrderTopic", "UpdateOrderQueue")
        sns_sqs_link("OrderProductionTopic", "OrderProductionQueue")