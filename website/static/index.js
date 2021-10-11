function deleteTestPC(testPcId) {
	fetch("/delete-test-pc", {
		method: "POST",
		body: JSON.stringify({ testPcId: testPcId }),
	}).then((_res) => {
		window.location.href = "/";
	});
}