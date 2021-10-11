function deleteTestPC(testPcId) {
	fetch("/delete-test-pc", {
		method: "POST",
		body: JSON.stringify({ testPcId: testPcId }),
	}).then((_res) => {
		window.location.href = "/";
	});
}

function deletePlatform(platformId) {
	fetch("/delete-platform", {
		method: "POST",
		body: JSON.stringify({ platformId: platformId }),
	}).then((_res) => {
		window.location.href = "/";
	});
}