from semantic_router import Route
from semantic_router.routers import SemanticRouter
from semantic_router.encoders import HuggingFaceEncoder


encoder = HuggingFaceEncoder(
    name="BAAI/bge-small-en-v1.5"
)

faq = Route(
    name="faq",
    utterances=[
        "What is the return policy of the products?",
        "Do I get discount with the HDFC credit card?",
        "How can I track my order?",
        "What payment methods are accepted?",
        "How long does it take to process a refund?",
        "How much does shipping cost?",
        "Can I cancel or change my order after placing it?",
        "Do you ship internationally?",
        "How do I contact customer support?",
        "What should I do if I receive a damaged or wrong item?",
        "Is there a warranty on your products?",
        "Where can I find the sizing guide?",
        "Do you offer free shipping?",
        "How can I use my promo code or gift card?"
    ],
)

sql = Route(
    name="sql",
    utterances=[
        "I want to buy nike shoes that have 50% discount.",
        "Are there any shoes under Rs. 3000?",
        "Do you have formal shoes in size 9?",
        "Are there any Puma shoes on sale?",
        "What is the price of puma running shoes?",
    ],
)

routes = [faq, sql]

router = SemanticRouter(encoder=encoder, routes=routes, auto_sync="local")
if __name__=="__main__":
    print(router("How long does it take to process a refund?").name)
    print(router("Pink Puma shoes in price range 500 to 1000").name)
