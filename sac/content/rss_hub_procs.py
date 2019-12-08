from sagas.graph.rss_hub import RssHub

class RssHubProcs(object):
    def prepare_seed(self, seed_conf='./rss/urls.txt'):
        """
        $ python -m sac.content.rss_hub_procs prepare_seed
        :return:
        """
        rsshub=RssHub(data_prefix='./rss/')
        rsshub.proc_resources(url_conf=seed_conf)
        rsshub.check_feeds(jsonify=True)

if __name__ == '__main__':
    import fire
    fire.Fire(RssHubProcs)


