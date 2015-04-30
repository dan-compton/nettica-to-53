from netticapy.api import DomainRecord
from netticapy.api import DnsApi
from subprocess import call

if __name__ == '__main__':
	api = DnsApi(username='', password='')
	domains = api.list_zones()
	DEBUG = False
	EXECUTE = True

	for domain in domains:
		try:
			print '------------------'
			print domain
			print '------------------'

			mx =[]

			for domain_record in api.list_domain(domain_name=domain):
				record = dict()
				record['domain_name'] = domain_record.domain_name
				record['host_name'] = domain_record.host_name
				record['type'] = domain_record.record_type
				record['ttl'] = str(domain_record.ttl)
				record['priority'] = str(domain_record.priority)
				record['data'] = str(domain_record.data)

				if record['type'] == 'A':
					hostname = ''
					if record['host_name'] is not None:
						hostname = record['host_name']
					if DEBUG:
						print['cli53', 'rrcreate', record['domain_name'], hostname, record['type'], record['data'], '--ttl', record['ttl']]
					if EXECUTE:
						call(['cli53', 'rrcreate', record['domain_name'], hostname, record['type'], record['data'], '--ttl', record['ttl']])

				elif record['type'] == 'CNAME':
					if DEBUG:
						print ['cli53', 'rrcreate', record['domain_name'], record['host_name'], record['type'], record['data']]
					if EXECUTE:
						call(['cli53', 'rrcreate', record['domain_name'], record['host_name'], record['type'], record['data']])

				elif record['type'] == 'MX':
					mx.append(record['priority'] + ' ' + record['data'])

				elif record['type'] == 'TXT':
					if DEBUG:
						print ['cli53' + ' ' + 'rrcreate' + ' ' + record['domain_name'] +' '+ record['type'] + ' ' +  record['data']]
					if EXECUTE:
						call(['cli53', 'rrcreate', record['domain_name'], '', record['type'], record['data']])

			if len(mx) > 0:
				params = ['cli53', 'rrcreate', record['domain_name'], '', 'MX']
				params.extend(mx)
				params.extend(['--ttl', record['ttl']])

				if DEBUG:
					print ['cli53' + ' ' + 'rrcreate' + ' ' +  record['domain_name'] +  ' ' +  mx  + ' ' + mxrecs, ' --ttl' + ' ' + record['ttl']]
				if EXECUTE:
					call(params)

		except KeyboardInterrupt:
			break
		except Exception, err:
			print Exception, err
			continue
