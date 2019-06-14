import prometheus_client as pc
from xmppwb.xmpp import XMPPBridgeBot


class Metrics:
    connection_active = pc.Gauge("xmppwb_xmpp_connection_active", "Indicates if the xmpp connection is still active (1)")
    messages_sent = pc.Counter("xmppwb_messages_sent", "Count of messages sent to xmpp muc")

    @classmethod
    def check_connection_active(cls, xmpp_client: XMPPBridgeBot):
        if xmpp_client.is_connected():
            cls.connection_active.set(1)
        else:
            cls.connection_active.set(0)

    @classmethod
    def increment_messages_sent(cls):
        cls.messages_sent.inc(1)